# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_fourwheelarm_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED fourwheelarm_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(fourwheelarm_FOUND FALSE)
  elseif(NOT fourwheelarm_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(fourwheelarm_FOUND FALSE)
  endif()
  return()
endif()
set(_fourwheelarm_CONFIG_INCLUDED TRUE)

# output package information
if(NOT fourwheelarm_FIND_QUIETLY)
  message(STATUS "Found fourwheelarm: 0.0.0 (${fourwheelarm_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'fourwheelarm' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${fourwheelarm_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(fourwheelarm_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${fourwheelarm_DIR}/${_extra}")
endforeach()
