import os

from conans import ConanFile, CMake, tools


class OpenDDSTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake", "virtualrunenv"

    requires = (
        "OpenDDS/3.14.0@camposs/stable"
        )

    def build(self):
        cmake = CMake(self)
        # Current dir is "test_package/build/<build_id>" and CMakeLists.txt is
        # in "test_package"
        cmake.configure()
        cmake.build()
