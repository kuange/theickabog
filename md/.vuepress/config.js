module.exports = {
  title: "TheIckabog - 中文阅读",
  description: "J.K.罗琳 新作 伊卡博格",
  themeConfig: {
    logo: "/story.png",
    nav: [
      { text: "首页", link: "/" },
      { text: "中文", link: "/chinese/" },
      { text: "English", link: "/english/" },
      { text: "Github", link: "https://github.com/kuange/theickabog" },
    ],
    search: true,
    searchMaxSuggestions: 10,
    sidebar: {
      "/chinese/": [
        "chapter-1",
        "chapter-2",
        "chapter-3",
        "chapter-4",
        "chapter-5",
        "chapter-6",
        "chapter-7",
        "chapter-8",
      ],
      "/english/": [
        "chapter-1",
        "chapter-2",
        "chapter-3",
        "chapter-4",
        "chapter-5",
        "chapter-6",
        "chapter-7",
        "chapter-8",
      ],
    },
  },
};
