#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class PicobenchConan(ConanFile):
    name = "picobench"
    version = "1.02"
    url = "https://github.com/bincrafters/conan-picobench"
    description = "A micro microbenchmarking library for C++11 in a single header file"
    
    # Indicates License type of the packaged library
    license = "https://github.com/iboB/picobench/blob/master/LICENSE.txt"
    
    # Packages the license for the conanfile.py
    exports = ["LICENSE.md"]
    
    # Custom attributes for Bincrafters recipe conventions
    source_folder = "source_folder"
    
    def source(self):
        source_url = "https://github.com/iboB/picobench"
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.version))
        extracted_dir = self.name + "-" + self.version

        #Rename to "source_folder" is a convention to simplify later steps
        #os.rename(extracted_dir, self.source_folder)


    def package(self):
        include_folder = os.path.join(self.name + "-" + self.version, "include")
        self.copy(pattern="LICENSE")
        self.copy(pattern="*", dst="include", src=include_folder)

    def package_id(self):
        self.info.header_only()
