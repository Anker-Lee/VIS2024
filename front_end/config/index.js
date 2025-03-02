// see http://vuejs-templates.github.io/webpack for documentation.
let path = require("path");
// let proxyPort = 5555;
let proxyPort = 7777;


module.exports = {
  build: {
    env: require("./prod.env"),
    index: path.resolve(__dirname, `../dist/index.html`),
    assetsRoot: path.resolve(__dirname, `../dist/`),
    assetsSubDirectory: "static",
    assetsPublicPath: `/`,
    productionSourceMap: false,
    // Gzip off by default as many popular static hosts such as
    // Surge or Netlify already gzip all static assets for you.
    // Before setting to `true`, make sure to:
    // npm install --save-dev compression-webpack-plugin
    productionGzip: false,
    productionGzipExtensions: ["js", "css"],
    // Run the build command with an extra argument to
    // View the bundle analyzer report after build finishes:
    // `npm run build --report`
    // Set to `true` or `false` to always turn it on or off
    bundleAnalyzerReport: process.env.npm_config_report
    //manifestFileName: 'manifest-doctor.json'
  },
  dev: {
    env: require("./dev.env"),
    port: 8050,
    assetsSubDirectory: "static",
    assetsPublicPath: "/",
    proxyTable: {
      '/rec': {//入参
        // target: `http://10.231.70.44:${proxyPort}`,
        target: "http://localhost:8080",
        changeOrigin: true,
        pathRewrite: {
          '^/rec': '/'//入参代理的Url
        }
      },
    },
    // CSS Sourcemaps off by default because relative paths are "buggy"
    // with this option, according to the CSS-Loader README 
    // (https://github.com/webpack/css-loader#sourcemaps)
    // In our experience, they generally work as expected,
    // just be aware of this issue when enabling this option.
    cssSourceMap: false
  }
};
