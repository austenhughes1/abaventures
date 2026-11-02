# abaventures.net

Static website for ABA Ventures LLC, hosted on GitHub Pages. It replaces the Squarespace site with the same pages, text and images. Plain HTML and CSS: nothing needs building before publishing.

```
index.html            Home
about/index.html      About
services/index.html   Services
contact/index.html    Contact (with the contact form)
css/style.css         All styling, measured from the Squarespace site
fonts/                Self-hosted Poppins (body) and Heebo (headings)
images/               Photos (optimized from the Squarespace originals)
404.html              Not-found page
work-1/, cart/        Redirects for old Squarespace URLs
tools/build_pages.py  Generates the HTML pages (shared header/footer live here)
```

The layout replicates the Squarespace theme rule for rule: the same fluid heading sizes, page gutters, section spacing, image-card layouts, mobile menu and form styling. It was checked against the live site at 1920, 1366, 1024, 800 and 390px wide, with every block, image, paragraph and form field within 1px.

**Editing:** small text changes can go straight into the page's HTML file. For bigger changes, edit `tools/build_pages.py` and run `python3 tools/build_pages.py .` from the repo root to regenerate all pages, so the header and footer stay in sync.

**Heading font:** Squarespace uses Acumin Pro, an Adobe font licensed only for Squarespace sites. The headings use Heebo (free, open-licensed), tuned to match Acumin's letter widths and stroke weight. If ABA ever gets an Adobe Fonts web project with Acumin Pro, add its `<link>` tag to the pages and it is used automatically. No CSS changes are needed.

**Contact form:** GitHub Pages can't process forms, so the form posts to [FormSubmit](https://formsubmit.co), a free service that emails submissions. They go to the address in `FORM_TO` in `tools/build_pages.py` (currently Austen@abaventures.net). **The first submission triggers a one-time activation email to that address. Click the link in it, or later submissions won't be delivered.** Submit a test message once the site is live.

## 1. Turn on GitHub Pages

Repo **Settings → Pages**:
- Source: **Deploy from a branch**
- Branch: **main**, folder **/ (root)**

The site will appear at `https://austenhughes1.github.io/abaventures/` within a minute or two. Links are relative, so the preview works before any DNS changes. Don't set a custom domain yet: once one is set, GitHub redirects the preview link to it.

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

3. In repo **Settings → Pages → Custom domain**, enter `www.abaventures.net` and save. GitHub adds a `CNAME` file to the repo. Once the DNS check passes, tick **Enforce HTTPS**. The certificate can take up to an hour.
4. Check `https://abaventures.net` and `https://www.abaventures.net` both load, then send yourself a test email to confirm mail still arrives.

## 3. Cancel the Squarespace website plan

Only after the new site is live on the domain: Squarespace site **Settings → Billing → Subscriptions → Website → Cancel**. This does not affect the domain or Google Workspace, which are billed separately.
