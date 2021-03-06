import tensorflow as tf
import numpy as np
import cv2
from mss import mss
from PIL import Image
import time
import platform
if platform.system()=='Windows':  
    from win32 import win32gui
    from ctypes import windll
    import win32ui

def getbackgroundwindowimage(hwnd, sx, sy):
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    w = right - left
    h = bot - top
    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()

    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, w-sx, h-sy)

    saveDC.SelectObject(saveBitMap)

    # Change the line below depending on whether you want the whole window
    # or just the client area. 
    result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 1)
    #result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 0)
    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)
    im = Image.frombuffer(
        'RGB',
        (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        bmpstr, 'raw', 'BGRX', 0, 1)
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)
    return im

    
tf.keras.backend.set_floatx('float16')
rgb_mean = np.array([0.4488, 0.4371, 0.4040]) * 255




def normalize(x, rgb_mean=rgb_mean):
    return (x - rgb_mean) / 127.5
def denormalize(x, rgb_mean=rgb_mean):
    return x * 127.5 + rgb_mean

inp=tf.keras.layers.Input((None,None,3))
x=tf.keras.layers.Lambda(normalize)(inp)
x0=tf.keras.layers.Conv2D(64,3,padding='same')(x)
x=x0
for i in range(4):
    y=tf.keras.layers.Conv2D(64,3,activation='relu',padding='same')(x)
    y=tf.keras.layers.Conv2D(64,3,padding='same')(y)
    x=tf.keras.layers.Add()([x,y])
x=tf.keras.layers.Conv2D(64,3,padding='same')(x)
x=tf.keras.layers.Add()([x0,x])
x=tf.keras.layers.Conv2D(48,3,padding='same')(x)
x=tf.keras.layers.Lambda (lambda z: tf.nn.depth_to_space(z, 4))(x)
out=tf.keras.layers.Lambda(denormalize)(x)
rtsrn=tf.keras.models.Model(inputs=inp, outputs=out)

rtsrn.load_weights('RTSR_NEAREST.h5')
rtsrm=tf.keras.models.clone_model(rtsrn)
rtsrm.load_weights('RTSR_MEDIAN.h5')
inp=rtsrn.input
out=tf.keras.backend.clip(rtsrn.output, 0, 255)
myclippededsrn=tf.keras.models.Model(inputs=inp, outputs=tf.cast(out, tf.uint8))
inp=rtsrm.input
out=tf.keras.backend.clip(rtsrm.output, 0, 255)
myclippededsrm=tf.keras.models.Model(inputs=inp, outputs=tf.cast(out, tf.uint8))
for i in range(7,0,-1):
    time.sleep(1)
    print ('make Game Window active for capturing, {} s. remains'.format(i))
if platform.system()=='Windows':  
    hwnd = win32gui.GetForegroundWindow()
    print(win32gui.GetForegroundWindow())
    #hwnd  = win32gui.FindWindowEx(None, None, None, 'test.jpg \u200e- Photos')

if False:
    def enum_window_titles():
        def callback(handle, data):
            titles.append(win32gui.GetWindowText(handle))

        titles = []
        win32gui.EnumWindows(callback, None)
        return titles


    titles = enum_window_titles()

    print(titles)


windname=win32gui.GetWindowText(hwnd)

pixels=[2,2]
shiftzero=[0,0]
windowsize=[0,0]
FPS=10.0
enhance=False
sct=mss()
resizemode=0
while True:
    starttime=time.time()
    if platform.system()=='Windows':  
        dimensions = win32gui.GetWindowRect(hwnd)
        #region=(dimensions[0]//8*8+shiftzero[0],dimensions[1]//8*8+shiftzero[1]+32,dimensions[2]//8*8+shiftzero[0]+windowsize[0],dimensions[3]//8*8+shiftzero[1]+windowsize[1]+32)
        screen=getbackgroundwindowimage(hwnd, shiftzero[0], shiftzero[1])
        imageinit=np.array(screen).copy()[:,:,::-1]

    #if (pixels[1]==2):
    if enhance==0:
        img3=np.array(Image.fromarray(imageinit).resize((imageinit.shape[1]*4//pixels[1],imageinit.shape[0]*4//pixels[0]),Image.NEAREST))
    if enhance==1:
        img2 = np.array(Image.fromarray(imageinit).resize((imageinit.shape[1]//pixels[1],imageinit.shape[0]//pixels[0]),Image.NEAREST))
        img3=myclippededsrm.predict(np.expand_dims(img2, 0))[0]
    if enhance==2:
        img2 = np.array(Image.fromarray(imageinit).resize((imageinit.shape[1]//pixels[1],imageinit.shape[0]//pixels[0]),Image.NEAREST))
        img3=myclippededsrn.predict(np.expand_dims(img2, 0))[0]
    img4=img3#.astype(np.uint8)
    #if resizemode==1:
    #    img5 = np.array(Image.fromarray(img4).resize((displaydims[0]-50,displaydims[1]-50)))
    if resizemode==0:
        img5=img4
    cv2.putText(img5,'FPS {:.2f} SR {}'.format(FPS, enhance),(30,30),cv2.FONT_HERSHEY_PLAIN, 1,(0,0,255),thickness=1)
    cv2.imshow('RTSR', img5)
    k = cv2.waitKey(1) 
    if k == ord('0'):
        enhance=(enhance+1)%3
    if k == ord('1'):
        pixels[1]=1
        pixels[0]=1
    if k == ord('2'):
        pixels[1]=2
        pixels[0]=2
    if k == ord('r'):
        resizemode=1-resizemode    
    if k == ord('w'):
        shiftzero[1]=shiftzero[1]+1
    if k == ord('s'):
        shiftzero[1]=shiftzero[1]-1
    if k == ord('a'):
        shiftzero[0]=shiftzero[0]+1
    if k == ord('d'):
        shiftzero[0]=shiftzero[0]-1
    if k == ord('k'):
        windowsize[1]=windowsize[1]+8
    if k == ord('i'):
        windowsize[1]=windowsize[1]-8
    if k == ord('j'):
        windowsize[0]=windowsize[0]+8
    if k == ord('l'):
        windowsize[0]=windowsize[0]-8
    if k == ord('q'):
        cv2.destroyAllWindows()
        break
    FPS=1/(time.time()-starttime)
