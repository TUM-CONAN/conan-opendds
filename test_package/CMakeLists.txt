# OpenDDS rtps discovery as C++11 test project from OpenDDS master branch

# conan is required hard, library name, version and description are configured from conan
if (EXISTS ${CMAKE_CURRENT_BINARY_DIR}/conanbuildinfo.cmake)
  include(${CMAKE_CURRENT_BINARY_DIR}/conanbuildinfo.cmake)
else ()
  message(FATAL_ERROR "The file conanbuildinfo.cmake doesn't exist, you have to run conan install first")
endif ()

project(OpenDDS_C++11_RTPS_Discovery CXX)

conan_basic_setup(TARGETS)

cmake_minimum_required(VERSION 3.8.2)

find_package(OpenDDS REQUIRED)

#set(CMAKE_CXX_COMPILER ${OPENDDS_COMPILER})
#set(target_prefix "opendds_cmake_cpp11_messenger_")
set(dst ${CMAKE_CURRENT_BINARY_DIR})

# IDL Library
set(idl "${target_prefix}idl")
add_library(${idl})
OPENDDS_TARGET_SOURCES(${idl} "TestMsg.idl" OPENDDS_IDL_OPTIONS "-Lc++11")
target_link_libraries(${idl} PUBLIC OpenDDS::Dcps)
set_target_properties(${idl} PROPERTIES
  RUNTIME_OUTPUT_DIRECTORY "${dst}/Idl"
)

# Assert the mapping used was C++11
get_property(mappings TARGET ${idl} PROPERTY OPENDDS_LANGUAGE_MAPPINGS)
if(NOT ("C++11" IN_LIST mappings))
  message(FATAL_ERROR "${idl}: C++11 NOT in mapping list: ${mappings}")
endif()

# Publisher
set(app_pub "publisher")
add_executable(${app_pub} "publisher.cpp")
target_link_libraries(${app_pub} PUBLIC CONAN_PKG::OpenDDS ${idl})

set(app_sub "subscriber")
add_executable(${app_sub} "subscriber.cpp" )
target_link_libraries(${app_sub} PUBLIC CONAN_PKG::OpenDDS ${idl})
