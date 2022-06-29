#include "lpch.h"
#include "Engine/Renderer/RenderCommand.h"
#include "Platform/OpenGL/OpenGLRendererAPI.h"

namespace Tookivi {

	RendererAPI* RenderCommand::s_RendererAPI = new OpenGLRendererAPI;

}