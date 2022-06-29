#pragma once
#include <imgui/imgui.h>
#include <imgui/imgui_internal.h>

#include "../UI.h"

namespace Tookivi {

	class MeshPanel
	{
	public:
		MeshPanel();
		~MeshPanel() = default;

		void DrawMesh(Entity& entity);

	private:

	};

}