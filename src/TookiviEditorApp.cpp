#include "lpch.h"
#include <Engine.h>
#include "Engine/Core/EntryPoint.h"
#include "EditorLayer.h"

namespace Tookivi {

	class TookiviEditorApp : public Application 
	{
	public:
		TookiviEditorApp() 
			:Application("Tookivi Editor")
		{
			PushLayer(new EditorLayer());
		}

		~TookiviEditorApp() {

		}

	};

	Application* CreateApplication() {
		return new TookiviEditorApp();
	}

}
