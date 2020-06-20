#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
from conans import CMake, ConanFile, AutoToolsBuildEnvironment, tools

class KinectAzureSensorSDKConan(ConanFile):
    name = "opendds"
    package_revision = ""
    upstream_version = "3.14.0"
    version = "{0}{1}".format(upstream_version, package_revision)
    generators = "make"
    settings =  "os", "compiler", "arch", "build_type"
    options = {"shared": [True, False]}
    default_options = "shared=True" # Must be present and must be build static (results in dynamic libraries)
    exports = [
        # "patches/CMakeLists.txt",
        #"patches/CMakeProjectWrapper.txt",
        # "patches/FindIconv.cmake",
        # "patches/FindLibXml2.cmake",
        # "patches/xmlversion.h.patch"
        "source_subfolder"
    ]
    url = "https://github.com/ulricheck/conan-azure-kinect-sensor-sdk"
    source_subfolder = "source_subfolder"
    build_subfolder = "build_subfolder"
    short_paths = True

    scm = {"revision": "branch-DDS-3.14",
           "subfolder": "source_subfolder",
           "submodule": "recursive",
           "type": "git",
           "url": "https://github.com/objectcomputing/OpenDDS.git"}



    def requirements(self):
        pass

    def build_requirements(self):
        pass

    def system_requirements____(self):
        # TODO install perl
        #if tools.os_info.is_linux:
        #    pack_names = [
        #        "libssl-dev",
        #        "uuid-dev",
        #        "libudev-dev",
        #        "libsoundio-dev",
        #        "nasm",
        #        "mono-devel",
        #    ]
        #    installer = tools.SystemPackageTool()
        #    for p in pack_names:
        #        installer.install(p)
        pass;

    def configure(self):
        # del self.settings.compiler.libcxx
        # if self.settings.os == "Windows" and not self.options.shared:
        #     self.output.warn("Warning! Static builds in Windows are unstable")
        #sdk_source_dir = os.path.join(self.build_folder, self.source_subfolder)
        
        pass

    def build(self):
        # fetch nuget package to extract depthengine shared library
        #tools.mkdir("nuget")
        #with tools.chdir("nuget"):
        #    if tools.os_info.is_linux:
        #        tools.download("https://dist.nuget.org/win-x86-commandline/latest/nuget.exe", "nuget.exe")
        #        self.run("mono nuget.exe install Microsoft.Azure.Kinect.Sensor -Version %s" % self.version)
        #    elif tools.os_info.is_windows:
        #        tools.download("https://dist.nuget.org/win-x86-commandline/latest/nuget.exe", "nuget.exe")
        #        
        #    else:
        #        raise NotImplementedError("unsupported platform")

        #sdk_source_dir = "/home/frieder/projects/conan_opendds/source_subfolder"
        #command = "cd %s" % sdk_source_dir
        #self.run(command + " && pwd")        
        #self.run(command + " && ./configure")
        #self.run(command + " && make")

        with tools.chdir(self.source_subfolder):
            self.run("pwd")
            self.run("./configure --prefix %s/%s" % (self.source_subfolder, "install"))
            self.run("make")
            self.run("make install")
        
        pass

    def package(self):        
        # self.copy("FindLibXml2.cmake", src="patches", dst=".", keep_path=False)
        pass

    def package_info(self):
        self.cpp_info.libdirs = ["source_subfolder/install/lib", "source_subfolder/ACE_wrappers/lib"]
        self.cpp_info.bindirs = ["source_subfolder/install/bin", "source_subfolder/ACE_wrappers/bin"]
        self.cpp_info.includedirs = ["source_subfolder/install/include", "source_subfolder/ACE_wrappers/include"]
        
        self.cpp_info.libs = tools.collect_libs(self)
        # if self.settings.os == "Linux" or self.settings.os == "Macos":
        #     self.cpp_info.libs.append('m')
        pass
   


def ConfigureOutput():
    """
    Welcome to OpenDDS version 3.14

    Options for this script are listed below, with the default behavior described
    in parenthesis after the option description.
    Boolean options can take the form "--opt" or "--no-opt", the more commonly
    needed one (the one that changes the default behavior) is shown below.
    Options that require arguments are shown as "--opt=VAL"  Options with optional
    arguments are shown as "--opt[=VAL]".  Options that can be repeated with
    cumulative effect are shown with a trailing "...".  Some third-party
    optional dependencies can be automatically located if they are installed in the
    expected locations (see entries below marked with "system pkg").  In those
    cases, specify the option as --opt without an = to enable the corresponding
    feature in OpenDDS and use the default installation location.

    Options controlling the configure script:
    --help                          Show this help and exit
    --target-help                   Show details of cross-compile target configs
    --verbose                       Trace script execution
    --dry-run                       Don't do anything
    --[no-]backup                   Make backup of build configuration files (yes)

    Build platform and compiler:
    --host=VAL                      Host (auto detect: linux, win32, solaris, macosx)
    --compiler=VAL                  Compiler (auto detect / guess by searching PATH)
    --std=VAL                       C++ standard version (for compilers that use -std)
    --target=VAL                    Cross-compile target (none): see --target-help
    --target-compiler=VAL           Compiler for target (if req'd): see --target-help
    --host-tools=VAL                DDS_ROOT of host tools for cross compile (build)
    --host-ace=VAL                  Define host ACE_ROOT (uses relative path from
                                    target DDS_ROOT to target ACE_ROOT)
    --host-tools-only               Just build the host tools (no)
    --prefix=VAL                    Installation prefix (none)

    Build flags:
    --[no-]debug                    Debugging (yes)
    --optimize                      Optimization (no)
    --[no-]inline                   Inlining (yes)
    --static                        Static libraries (no)
    --ipv6                          IPv6 support (no)

    Required dependencies for OpenDDS:
    --ace=VAL                       ACE (use ACE_ROOT, ACE_wrappers, or download)
    --tao=VAL                       TAO (use TAO_ROOT, ACE_ROOT/TAO, or download)
    --mpc=VAL                       MPC (use MPC_ROOT, ACE_ROOT/MPC, or download)
    --doc-group                     Use the DOC Group release of TAO (no)
    --ace-github-latest             Clone latest ACE/TAO/MPC from GitHub (no)
    --force-ace-tao                 Force configuration of ACE/TAO (no)

    Advanced configuration:
    --configh=VAL...                Extra text for config.h
    --macros=VAL...                 Extra text for platform_macros.GNU
    --features=VAL...               Extra text for default.features
    --mpcopts=VAL...                Extra command-line args for MPC

    Optional dependencies for OpenDDS (disabled by default unless noted otherwise):
    --java[=VAL]                    Java development kit (use JAVA_HOME)
    --jboss[=VAL]                   JBoss application server (use JBOSS_HOME)
    --ant[=VAL]                     Ant for JBoss (use ANT_HOME or system pkg)
    --wireshark[=VAL]               Wireshark dev headers or source not built with
                                    CMake (use WIRESHARK_SRC or system pkg)
                                    Implies --glib
    --wireshark-cmake[=VAL]         Wireshark source built with CMake, requires
                                    --wireshark-build. Requires --wireshark-lib if
                                    guessing fails (use WIRESHARK_SRC)
                                    Implies --glib
    --wireshark-build=VAL           Wireshark CMake Build Location
    --wireshark-lib=VAL             Optional Wireshark CMake libraries location
                                    relative to wireshark-build (guesses)
    --glib[=VAL]                    GLib for Wireshark (use GLIB_ROOT or system pkg)
    --[no-]rapidjson[=VAL]          RapidJSON for Wireshark dissector and JSON
                                    Sample Serialization (Enabled by default,
                                    use git submodle, RAPIDJSON_ROOT, or system pkg)
    --qt[=VAL]                      Qt5 (use QTDIR or system pkg)
    --qt-include[=VAL]              Qt include dir (use QT5_INCDIR, QTDIR/include,
                                    or sysytem package)
    --boost[=VAL]                   Boost (use BOOST_ROOT or system pkg)
    --boost-version[=VAL]           Boost version (only if needed to find headers)
    --xerces3[=VAL]                 Xerces-C++ 3 for QoS XML handling, DDS Security
    --openssl[=VAL]                 OpenSSL for DDS Security
    --cmake[=VAL]                   Path to cmake binary for compiling Google Test
                                    Framework. (Check Path and Check Normal
                                    Locations)
    --gtest=VAL                     Path to Google Test Framework, required for
                                    tests (uses GTEST_ROOT).
                                    If not built, will try to build using CMake.

    Optional OpenDDS features:
    --[no-]built-in-topics          Built-in Topics (yes)
    --[no-]content-subscription     Content-Subscription Profile (yes)
    --[no-]content-filtered-topic   ContentFilteredTopic (CS Profile) (yes)
    --[no-]multi-topic              MultiTopic (CS Profile) (yes)
    --[no-]query-condition          QueryCondition (CS Profile) (yes)
    --[no-]ownership-profile        Ownership Profile (yes)
    --[no-]ownership-kind-exclusive Exclusive Ownership (Ownership Profile) (yes)
    --[no-]object-model-profile     Object Model Profile (yes)
    --[no-]persistence-profile      Persistence Profile (yes)
    --safety-profile[=VAL]          Safety Profile: base or extended (none)
    --tests                         Build tests, examples, and performance tests (no)
                                    Requires --gtest if missing git submodule
    --security                      DDS Security plugin (no) Implies --openssl and
                                    --xerces3

    """
    pass