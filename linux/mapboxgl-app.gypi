{
  'includes': [
    '../gyp/common.gypi',
  ],
  'targets': [
    { 'target_name': 'linuxapp',
      'product_name': 'mbgl-app',
      'type': 'executable',

      'dependencies': [
        '../mbgl.gyp:mbgl',
      ],

      'sources': [
        'main.cpp',
        '../platform/default/settings_json.cpp',
        '../platform/default/glfw_view.hpp',
        '../platform/default/glfw_view.cpp',
        '../platform/default/log_stderr.cpp',
        '../platform/default/default_styles.hpp',
        '../platform/default/default_styles.cpp',
      ],

      'variables' : {
        'cflags_cc': [
          '<@(glfw3_cflags)',
        ],
        'ldflags': [
          '<@(glfw3_ldflags)',
        ],
        'libraries': [
          '<@(glfw3_static_libs)',
          '-lboost_filesystem',
          '-lboost_system'
        ],
      },

      'conditions': [
        ['OS == "mac"', {
          'libraries': [ '<@(libraries)' ],
          'xcode_settings': {
            'SDKROOT': 'macosx',
            'SUPPORTED_PLATFORMS':'macosx',
            'OTHER_CPLUSPLUSFLAGS': [ '<@(cflags_cc)' ],
            'OTHER_LDFLAGS': [ '<@(ldflags)' ],
            'SDKROOT': 'macosx',
            'MACOSX_DEPLOYMENT_TARGET': '10.9',
          }
        }, {
          'cflags_cc': [ '<@(cflags_cc)' ],
          'libraries': [ '<@(libraries)', '<@(ldflags)' ],
        }]
      ],
    },
  ],
}
