# abaventures.net

Static website for ABA Ventures LLC, hosted on GitHub Pages. It replaces the Squarespace site with the same pages, text and images. Plain HTML and CSS, with no build step.

```
index.html            Home
about/index.html      About
services/index.html   Services
contact/index.html    Contact
css/style.css         All styling
images/               Photos (optimized from the Squarespace originals)
404.html              Not-found page
work-1/, cart/        Redirects for old Squarespace URLs
CNAME                 Custom domain (www.abaventures.net)
```

To edit text, change the HTML file for that page and commit. GitHub Pages republishes within a minute or two. The header and footer are repeated in each page, so a nav change has to be made in all four.

## 1. Turn on GitHub Pages

Repo **Settings → Pages**:
- Source: **Deploy from a branch**
- Branch: **main**, folder **/ (root)**

The site will appear at `https://austenhughes1.github.io/abaventures/` to preview. Links are relative, so the preview works before DNS changes. The `CNAME` file sets the custom domain to `www.abaventures.net`.

Recommended: verify the domain under **GitHub profile Settings → Pages → Add a domain**, which adds a TXT record. This stops anyone else from claiming the domain on GitHub.

## 2. Point the domain at GitHub (do this when ready to switch)

The domain's DNS lives in the **Squarespace Domains** account (account.squarespace.com/domains), the same one billing Google Workspace.

**Do not touch the MX, DKIM (`google._domainkey`), or `google-site-verification` TXT records.** Those carry company email.

1. Remove the Squarespace website records: the `@` A records pointing at Squarespace and the `www` CNAME to `ext-cust.squarespace.com`. In Squarespace this may show as "Squarespace Defaults". Delete only the website entries, not the Google Workspace ones.
2. Add:

| Host | Type | Value |
|------|------|-------|
| @ | A | 185.199.108.153 |
| @ | A | 185.199.109.153 |
| @ | A | 185.199.110.153 |
| @ | A | 185.199.111.153 |
| @ | AAAA | 2606:50c0:8000::153 |
| @ | AAAA | 2606:50c0:8001::153 |
| @ | AAAA | 2606:50c0:8002::153 |
| @ | AAAA | 2606:50c0:8003::153 |
| www | CNAME | austenhughes1.github.io |

3. In repo **Settings → Pages**, confirm the custom domain shows `www.abaventures.net`. Once the DNS check passes, tick **Enforce HTTPS**. The certificate can take up to an hour.
4. Check `https://abaventures.net` and `https://www.abaventures.net` both load, then send yourself a test email to confirm mail still arrives.

## 3. Cancel the Squarespace website plan

Only after the new site is live on the domain: Squarespace site **Settings → Billing → Subscriptions → Website → Cancel**. This does not affect the domain or Google Workspace, which are billed separately.
