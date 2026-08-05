import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
  site: 'https://janilbols-w.github.io',
  base: '/weekly-paper',
  integrations: [
    starlight({
      title: 'Efficient Inference & AI Infra Papers',
      description: '每周精选 LLM 高效推理与 AI Infra 论文',
      social: [
        { icon: 'github', label: 'GitHub', href: 'https://github.com/janilbols-w/weekly-paper' }
      ],
      customCss: ['./src/styles/custom.css'],
      sidebar: [
        { label: '开始', items: [
          { label: '首页', slug: 'index' },
          { label: '论文知识地图', slug: 'explorer' },
          { label: '累计统计', slug: 'stats' },
          { label: '方法与评分', slug: 'methodology' }
        ]},
        { label: '每周简报', items: [{ autogenerate: { directory: 'weekly' } }] },
        { label: '三级主题', items: [{ autogenerate: { directory: 'topics' } }] },
        { label: '论文详情', collapsed: true, items: [{ autogenerate: { directory: 'papers' } }] }
      ]
    })
  ]
});
