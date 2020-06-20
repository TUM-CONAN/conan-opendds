from conans import CMake, ConanFile, AutoToolsBuildEnvironment, tools

class OpenDDSConan(ConanFile):
    name = "OpenDDS"
    version = "3.14.0"
    license = "OpenDDS license"
    author = "Frieder Pankratz"
    url = "https://github.com/TUM-CONAN/conan-opendds.git"
    description = "Conan wrapper for OpenDDS"
    #topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": True}
    generators = "cmake"

    def source(self):
        git = tools.Git()
        #git.clone("https://github.com/objectcomputing/OpenDDS.git", "branch-DDS-3.14")        
        git.clone("https://github.com/objectcomputing/OpenDDS.git", "master")

    def build(self):
        if tools.os_info.is_linux:
            atools = AutoToolsBuildEnvironment(self)
            atools.configure(args=["--ace-github-latest"])        
            atools.install()
        elif tools.os_info.is_windows:
            self.run('./configure.cmd --ace-github-latest')
            # TODO build visual studio project
        else:
            raise NotImplementedError("unsupported platform")
        

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)

