#pragma once

#include "Core.h"
#pragma warning(push, 0)
#include <spdlog/spdlog.h>
#include <spdlog/fmt/ostr.h>
#pragma warning(pop)

namespace Tookivi {
	class Log
	{
	public:

		static void init();
		inline static std::shared_ptr<spdlog::logger>& GetCoreLogger() { return s_CoreLogger; }
		inline static std::shared_ptr<spdlog::logger>& GetClientLogger() { return s_ClientLogger; }

	private:
		static std::shared_ptr<spdlog::logger> s_CoreLogger;
		static std::shared_ptr<spdlog::logger> s_ClientLogger;

	};
}

// core log macros
#define SN_CORE_ERROR(...)  ::Tookivi::Log::GetCoreLogger()->error(__VA_ARGS__)
#define SN_CORE_WARN(...)	::Tookivi::Log::GetCoreLogger()->warn(__VA_ARGS__)
#define SN_CORE_TRACE(...)	::Tookivi::Log::GetCoreLogger()->trace(__VA_ARGS__)
#define SN_CORE_INFO(...)	::Tookivi::Log::GetCoreLogger()->info(__VA_ARGS__)
#define SN_CORE_FATAL(...)	::Tookivi::Log::GetCoreLogger()->fatal(__VA_ARGS__)
			 
// client log macros		 
#define SN_ERROR(...)		::Tookivi::Log::GetClientLogger()->error(__VA_ARGS__)
#define SN_WARN(...)		::Tookivi::Log::GetClientLogger()->warn(__VA_ARGS__)
#define SN_TRACE(...)		::Tookivi::Log::GetClientLogger()->trace(__VA_ARGS__)
#define SN_INFO(...)		::Tookivi::Log::GetClientLogger()->info(__VA_ARGS__)
#define SN_FATAL(...)		::Tookivi::Log::GetClientLogger()->fatal(__VA_ARGS__)



