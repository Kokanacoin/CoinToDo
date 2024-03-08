module.exports = {
    devServer: {
        open: true,
        port: 8080,
        https: false,
        proxy: {
            '/api': {
                target: 'http://localhost:8000/api',  // target host
                ws: true,  // proxy websockets 
                changeOrigin: true,  // needed for virtual hosted sites
                pathRewrite: {
                    '^/api': ''  // rewrite path
                }
            },
        }
    }  
};

