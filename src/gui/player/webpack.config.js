'use strict'

const path = require('path')
const autoprefixer = require('autoprefixer')
const HtmlWebpackPlugin = require('html-webpack-plugin')
const webpack = require('webpack')
const TerserPlugin = require('terser-webpack-plugin');

module.exports = (env, argv) => {
    const isProduction = argv.mode === 'production';

    return {
        mode: 'development',
        entry: './src/js/main.js',
        output: {
            filename: 'main.js',
            path: path.resolve(__dirname, '../../../gui/player'),
            publicPath: isProduction ? '/player/' : '/',
        },
        devServer: {
            static: path.resolve(__dirname),
            port: 8081,
            hot: true,
            historyApiFallback: {
                index: '/player/index.html'
            }
        },
        plugins: [
            new webpack.DefinePlugin({
                'process.env.NODE_ENV': JSON.stringify(argv.mode),
            }),
            new webpack.ProvidePlugin({
                $: 'jquery',
                jQuery: 'jquery'
            }),
            new HtmlWebpackPlugin({
                template: './src/index.html',
                inject: "head",
                scriptLoading: 'blocking',
            }),
        ],
        module: {
            rules: [
                {
                    test: /\.(scss)$/,
                    use: [
                        {
                            // Adds CSS to the DOM by injecting a `<style>` tag
                            loader: 'style-loader'
                        },
                        {
                            // Interprets `@import` and `url()` like `import/require()` and will resolve them
                            loader: 'css-loader'
                        },
                        {
                            // Loader for webpack to process CSS with PostCSS
                            loader: 'postcss-loader',
                            options: {
                                postcssOptions: {
                                    plugins: [
                                        autoprefixer
                                    ]
                                }
                            }
                        },
                        {
                            // Loads a SASS/SCSS file and compiles it to CSS
                            loader: 'sass-loader'
                        }
                    ]
                }
            ]
        },
        optimization: {
            minimizer: [
                new TerserPlugin({
                    extractComments: false,
                    terserOptions: {
                        format: {
                            comments: false,
                        },
                    },
                }),
            ],
        },
    }
}
