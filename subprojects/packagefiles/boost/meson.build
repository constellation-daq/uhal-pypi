project(
  'boost',
  'cpp',
  version: '1.90.0',
  license: 'BSL-1.0',
  default_options: ['cpp_std=c++20', 'warning_level=0'],
)

boost_headers_inc = include_directories('.')
boost_headers_dep = declare_dependency(
  include_directories: boost_headers_inc,
)

# We also need to compile the filesystem module

boost_filesystem_src = files(
  'libs/filesystem/src/codecvt_error_category.cpp',
  'libs/filesystem/src/directory.cpp',
  'libs/filesystem/src/exception.cpp',
  'libs/filesystem/src/operations.cpp',
  'libs/filesystem/src/path.cpp',
  'libs/filesystem/src/path_traits.cpp',
  'libs/filesystem/src/portability.cpp',
  'libs/filesystem/src/unique_path.cpp',
  'libs/filesystem/src/utf8_codecvt_facet.cpp',
)
boost_filesystem_lib = static_library(
  'boost_filesystem',
  sources: boost_filesystem_src,
  include_directories: boost_headers_inc,
)
boost_filesystem_dep = declare_dependency(
  link_with: boost_filesystem_lib,
  include_directories: boost_headers_inc,
)
