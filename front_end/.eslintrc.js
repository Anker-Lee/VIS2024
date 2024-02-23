module.exports = {
    "root": true,
    "env": {
        "browser": true,
        "node": true,
        "es6": true
    },
    "plugins": ["vue"],
    "settings": {
        "html/html-extensions": [".html", ".vue", ".php", ".twig"]
    },
    "parserOptions": {
        "ecmaVersion": 2017,
        "sourceType": "module",
        "ecmaFeatures": {
            "impliedStrict": true,
            "experimentalObjectRestSpread": true
        }
    },
    "globals": {
        "ajax": true,
        "axios": true,
        "Tether": true,
        "Promise": true,
        "d3": true
    },
    "extends": ["eslint:recommended", "plugin:vue/recommended"],
    "rules": {


    }
}