#pragma once
#include <imgui/imgui.h>
#include <imgui/imgui_internal.h>

#include "../UI.h"

namespace Tookivi {

	class LightPanel {

	public:
		LightPanel();
		~LightPanel() = default;

		void DrawLight(Entity& entity);

	};

}