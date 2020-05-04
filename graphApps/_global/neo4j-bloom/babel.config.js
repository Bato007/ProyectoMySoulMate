module.exports = {
  presets: ['@babel/preset-env', '@babel/preset-react'],
  plugins: [
    ['babel-plugin-styled-components', {
      'ssr': false,
      'displayName': true,
      'fileName': false
    }],
    'transform-object-rest-spread',
    '@babel/plugin-proposal-class-properties'
  ]
}
