#pragma once
#include "Application.h"


#ifdef SN_PLATFORM_WINDOWS

extern Tookivi::Application* Tookivi::CreateApplication();
extern "C" {
	__declspec(dllexport) uint32_t NvOptimusEnablement = 0x00000001;
}

int main(int argc, char** argv) 
{
	Tookivi::Log::init();
	SN_WARN("HELLO! Welcome to Tookivi!");

	auto app = Tookivi::CreateApplication();
	app->Run();
	delete app;
}

#endif // SN_PLATFORM_WINDOWS
