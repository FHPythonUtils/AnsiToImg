
# FAQs

**Q: Why does the font look off when using AnsiToImg, especially on Android or other platforms?**

AnsiToImg cannot meaningfully control the font used when rendering text, as it relies on the OS
and the Playwright library (which uses the Chromium browser to render SVGs). This means that font
rendering issues, such as alignment problems or incorrect fonts, are often caused by the system's
font fallback mechanisms.

Android users may particularly notice this issue due to how Android handles font fallbacks.
Unfortunately, this is not something AnsiToImg can directly control. The issue stems from upstream,
meaning it would need to be resolved by the Android platform itself.

For more in-depth information about font fallback issues, I recommend reading articles by **Tonsky**,
the creator of Fira Code. They explain these kinds of problems much better than I could. You can
check out one of their posts here: [Font Size Article by Tonsky](https://tonsky.me/blog/font-size/).

Here's another example of a similar alignment issue in a different project:
[Nushell Issue #83](https://github.com/nushell/nushell.github.io/issues/83). In that case, the
developers also faced limitations due to upstream dependencies.
