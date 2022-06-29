#pragma once

#include <glm/glm.hpp>

namespace Tookivi::Math {

	//************************************
	// Method:    DecomposeTransform
	// FullName:  Tookivi::Math::DecomposeTransform
	// Access:    public 
	// Returns:   bool
	// Qualifier:
	// Parameter: const glm::mat4 & transform
	// Parameter: glm::vec3 & translation
	// Parameter: glm::vec3 & rotation
	// Parameter: glm::vec3 & scale
	// Author: The cherno
	//************************************
	bool DecomposeTransform(const glm::mat4& transform, glm::vec3& translation, glm::vec3& rotation, glm::vec3& scale);

}