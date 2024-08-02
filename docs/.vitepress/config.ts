export default {
    title: 'pdgen Documentation',
    head: [['link', {rel: 'icon', href: 'https://softoft.sirv.com/pdgen/pdgen-python-logo-v4-black.png'}]],
    description: 'Automatically generate UML class diagrams from Python code with pdgen.',
    base: '/',
    sitemap: {
        hostname: '',
    },
    themeConfig: {
        nav: [{text: 'Home', link: '/'}, {
            text: 'Guide',
            items: [{text: 'Introduction', link: '/guide/introduction'}, {
                text: 'Installation',
                link: '/guide/installation'
            }, {text: 'Usage', link: '/guide/usage'}, {
                text: 'Configuration',
                link: '/guide/configuration'
            }, {text: 'Advanced Features', link: '/guide/advanced'}, {
                text: 'Python - UML Diagram',
                link: '/guide/uml-diagram'
            },]
        }, {text: 'GitHub', link: 'https://github.com/softoft/pdgen'}],

        sidebar: {
            '/guide/': [{
                text: 'Guide',
                children: [{text: 'Introduction', link: '/guide/introduction'}, {
                    text: 'Installation',
                    link: '/guide/installation'
                }, {text: 'Usage', link: '/guide/usage'}, {
                    text: 'Configuration',
                    link: '/guide/configuration'
                }, {text: 'Advanced Features', link: '/guide/advanced'}, {
                    text: 'Python - UML Diagram',
                    link: '/guide/uml-diagram'
                },]
            }],
        }
    }
}
