project(
  'ipbus-software',
  'cpp',
  version: '2.8.22',
  license: 'GPL-3.0-only',
  default_options: ['warning_level=0', 'default_library=static'],
)

uhal_version_list = meson.project_version().split('.')
uhal_version_major = uhal_version_list[0]
uhal_version_minor = uhal_version_list[1]
uhal_version_patch = uhal_version_list[2]

boost_sp = subproject('boost')
boost_headers_dep = boost_sp.get_variable('boost_headers_dep')
boost_filesystem_dep = boost_sp.get_variable('boost_filesystem_dep')
pugixml_dep = dependency('pugixml', default_options: ['default_library=static'])
threads_dep = dependency('threads')
rt_dep = meson.get_compiler('cpp').find_library('rt')

# grammars

uhal_grammars_inc = include_directories(
  'uhal/grammars/include',
  'uhal/grammars/include/uhal/grammars',
)
uhal_grammars_src = files(
  'uhal/grammars/src/common/HttpResponseGrammar.cpp',
  'uhal/grammars/src/common/NodeTreeClassAttributeGrammar.cpp',
  'uhal/grammars/src/common/NodeTreeFirmwareInfoAttributeGrammar.cpp',
  'uhal/grammars/src/common/NodeTreeParametersGrammar.cpp',
  'uhal/grammars/src/common/SemicolonDelimitedUriListGrammar.cpp',
  'uhal/grammars/src/common/URI.cpp',
  'uhal/grammars/src/common/URIGrammar.cpp',
)
uhal_grammars_lib = library(
  'cactus_uhal_grammars',
  sources: uhal_grammars_src,
  include_directories: uhal_grammars_inc,
  dependencies: boost_headers_dep,
  install: true,
)
uhal_grammars_dep = declare_dependency(
  link_with: uhal_grammars_lib,
  include_directories: uhal_grammars_inc,
  dependencies: boost_headers_dep,
)

# log

uhal_log_inc = include_directories(
  'uhal/log/include',
  'uhal/log/include/uhal/log',
)
uhal_log_src = files(
  'uhal/log/src/common/LogLevels.cpp',
  'uhal/log/src/common/exception.cpp',
  'uhal/log/src/common/log.cpp',
  'uhal/log/src/common/log_inserters.integer.cpp',
  'uhal/log/src/common/log_inserters.location.cpp',
  'uhal/log/src/common/log_inserters.quote.cpp',
  'uhal/log/src/common/log_inserters.threadID.cpp',
  'uhal/log/src/common/log_inserters.time.cpp',
)
uhal_log_lib = library(
  'cactus_uhal_log',
  sources: uhal_log_src,
  include_directories: uhal_log_inc,
  cpp_args: ['-DMAX_NUM_ARGS=32'],
  dependencies: [boost_headers_dep, threads_dep],
  install: true,
)
uhal_log_dep = declare_dependency(
  link_with: uhal_log_lib,
  include_directories: uhal_log_inc,
)

# uhal

generate_version = find_program('generate_version.py')
subdir('uhal/uhal/include/uhal')
subdir('uhal/uhal/src/common')

uhal_uhal_inc = include_directories(
  'uhal/uhal/include',
  'uhal/uhal/include/uhal',
  'uhal/uhal/templates',
)
uhal_uhal_src = files(
  'uhal/uhal/src/common/Buffers.cpp',
  'uhal/uhal/src/common/ClientFactory.cpp',
  'uhal/uhal/src/common/ClientInterface.cpp',
  'uhal/uhal/src/common/ConnectionManager.cpp',
  'uhal/uhal/src/common/DerivedNodeFactory.cpp',
  'uhal/uhal/src/common/HwInterface.cpp',
  'uhal/uhal/src/common/IPbusInspector.cpp',
  'uhal/uhal/src/common/Node.cpp',
  'uhal/uhal/src/common/NodeTreeBuilder.cpp',
  'uhal/uhal/src/common/ProtocolControlHub.cpp',
  'uhal/uhal/src/common/ProtocolIPbus.cpp',
  'uhal/uhal/src/common/ProtocolIPbusCore.cpp',
  'uhal/uhal/src/common/ProtocolMmap.cpp',
  'uhal/uhal/src/common/ProtocolPCIe.cpp',
  'uhal/uhal/src/common/ProtocolTCP.cpp',
  'uhal/uhal/src/common/ProtocolUDP.cpp',
  'uhal/uhal/src/common/SigBusGuard.cpp',
  'uhal/uhal/src/common/ValMem.cpp',
  'uhal/uhal/src/common/detail/PacketFmt.cpp',
  'uhal/uhal/src/common/detail/RobustSessionMutex.cpp',
  'uhal/uhal/src/common/detail/SharedObject.cpp',
  'uhal/uhal/src/common/detail/utilities.cpp',
  'uhal/uhal/src/common/utilities/TimeIntervalStats.cpp',
  'uhal/uhal/src/common/utilities/bits.cpp',
  'uhal/uhal/src/common/utilities/files.cpp',
  'uhal/uhal/src/common/utilities/xml.cpp',
)
uhal_uhal_lib = library(
  'cactus_uhal_uhal',
  sources: [uhal_uhal_src, uhal_uhal_version_hpp, uhal_uhal_version_cpp],
  include_directories: uhal_uhal_inc,
  dependencies: [
    uhal_grammars_dep,
    uhal_log_dep,
    boost_headers_dep,
    boost_filesystem_dep,
    pugixml_dep,
    threads_dep,
    rt_dep,
  ],
  install: true,
)
uhal_uhal_dep = declare_dependency(
  link_with: uhal_uhal_lib,
  include_directories: uhal_uhal_inc,
  dependencies: [
    uhal_grammars_dep,
    uhal_log_dep,
    boost_headers_dep,
    boost_filesystem_dep,
    pugixml_dep,
  ],
)

# tests

uhal_tests_inc = include_directories(
  'uhal/tests/include',
  'uhal/tests/include/uhal/tests',
)
uhal_tests_src = files(
  'uhal/tests/src/common/DummyHardware.cpp',
  'uhal/tests/src/common/tools.cpp',
)
uhal_tests_lib = library(
  'cactus_uhal_tests',
  sources: uhal_tests_src,
  include_directories: uhal_tests_inc,
  dependencies: [uhal_log_dep, uhal_uhal_dep, threads_dep, rt_dep],
  install: true,
)
uhal_tests_dep = declare_dependency(
  link_with: uhal_tests_lib,
  include_directories: uhal_tests_inc,
)

# python

python = import('python').find_installation(pure: false)
pybind11_dep = dependency('pybind11')

uhal_python_inc = include_directories(
  'uhal/python/include',
  'uhal/python/include/uhal/pycohal',
)
uhal_python_src = files(
  'uhal/python/src/common/cactus_pycohal.cpp',
  'uhal/python/src/common/enums_logging.cpp',
  'uhal/python/src/common/exceptions.cpp',
  'uhal/python/src/common/version.cpp',
)
python.extension_module(
  '_core',
  subdir: 'uhal',
  sources: uhal_python_src,
  include_directories: uhal_python_inc,
  dependencies: [uhal_log_dep, uhal_uhal_dep, uhal_tests_dep, pybind11_dep],
  install: true,
)
python.install_sources(
  'uhal/python/pkg/uhal/__init__.py',
  subdir: 'uhal',
)
