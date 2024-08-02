export default {
    title: 'pdgen Documentation',
    head: [
        ['link', { rel: 'icon', href: 'https://softoft.sirv.com/pdgen/pdgen-python-logo-v4-black.png' }]
    ],
    description: 'Automatically generate UML class diagrams from Python code with pdgen.',
    base: '/',
    sitemap: {
        hostname: 'https://python-diagram-generator.com/',
    },
    themeConfig: {
        repo: 'https://github.com/yourusername/pdgen',
        docsDir: 'docs',
        lastUpdated: 'Last Updated',

        nav: [
            { text: 'Home', link: '/' },
            { text: 'Guide', link: '/guide/' },
            { text: 'GitHub', link: 'https://github.com/softoft/pdgen' }
        ],

        sidebar: {
            '/guide/': [
                {
                    text: 'Guide',
                    children: [
                        { text: 'Introduction', link: '/guide/introduction' },
                        { text: 'Installation', link: '/guide/installation' },
                        { text: 'Usage', link: '/guide/usage' },
                        { text: 'Configuration', link: '/guide/configuration' },
                        { text: 'Advanced Features', link: '/guide/advanced' }
                    ]
                }
            ],
        }
    }
}
