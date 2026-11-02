"""Generates the static pages for abaventures.net. Run: python3 make.py <output dir>"""
import os
import sys

OUT = sys.argv[1]
SITE = "https://www.abaventures.net"
NAV = [("", "Home"), ("about/", "About"), ("services/", "Services"), ("contact/", "Contact")]
FOOT = [("", "Home"), ("about/", "About Us"), ("services/", "Services"), ("contact/", "Contact Us")]
FORM_TO = "Austen@abaventures.net"  # where Contact form submissions are emailed


def page(slug, title, desc, body, pre=None, path=None, extra_head=""):
    if pre is None:
        pre = "../" if slug else ""
    home = pre or "./"
    nav = "".join(
        f'<a href="{pre}{h}"{" aria-current=\"page\"" if h == slug else ""}>{t}</a>' for h, t in NAV)
    menu = "".join(f'<li><a href="{pre}{h}">{t}</a></li>' for h, t in NAV)
    foot = "<br>".join(f'<a href="{pre}{h}">{t}</a>' for h, t in FOOT)
    full_title = "ABA Ventures" if not slug else f"{title} &mdash; ABA Ventures"
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{full_title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{SITE}/{slug}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="ABA Ventures">
  <meta property="og:title" content="{full_title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{SITE}/{slug}">
  <meta property="og:image" content="{SITE}/images/hero-tower.jpg">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="{pre}favicon.svg" type="image/svg+xml">
  <link rel="preload" href="{pre}fonts/poppins-300-latin.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="{pre}fonts/heebo-latin.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="{pre}css/style.css">{extra_head}
</head>
<body>
  <a class="skip" href="#main">Skip to Content</a>
  <header class="header">
    <div class="header-inner">
      <p class="site-title"><a href="{home}">ABA Ventures</a></p>
      <nav class="nav" aria-label="Main">{nav}</nav>
      <button class="burger" type="button" aria-label="Open Menu" aria-expanded="false" aria-controls="mobile-menu"><span class="burger-box"><span></span><span></span></span></button>
    </div>
    <nav class="mobile-menu" id="mobile-menu" aria-label="Mobile"><ul>{menu}</ul></nav>
  </header>

  <main id="main">
{body.replace('{pre}', pre)}
  </main>

  <footer class="footer">
    <section class="section small">
      <div class="wrap"><div class="content medium">
        <div class="block">
          <h3>ABA</h3>
          <p>{foot}</p>
          <p><br></p>
        </div>
      </div></div>
    </section>
  </footer>

  <script>
    (function () {{
      var b = document.querySelector(".burger");
      b.addEventListener("click", function () {{
        var open = document.body.classList.toggle("menu-open");
        b.setAttribute("aria-expanded", open);
        b.setAttribute("aria-label", open ? "Close Menu" : "Open Menu");
      }});
    }})();
  </script>
</body>
</html>
"""
    path = os.path.join(OUT, path or os.path.join(slug, "index.html"))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(html)
    print("wrote", path)


def bullets(items):
    return "".join(f"<li><p>{i}</p></li>" for i in items)


def figure(kind, flip, img, alt, w, h, title, sub):
    t = f"<h3><strong>{title}</strong></h3>" if title else ""
    return f"""          <div class="block">
            <figure class="figure {kind}{' flip' if flip else ''}">
              <div class="media"><img src="{{pre}}images/{img}" alt="{alt}" width="{w}" height="{h}" loading="lazy"></div>
              <figcaption class="card">
                <div class="title">{t}</div>
                <div class="sub">{sub}</div>
              </figcaption>
            </figure>
          </div>"""


SPACER = '          <div class="block spacer" aria-hidden="true"></div>'

HOME = """    <section class="section medium theme-image">
      <div class="section-bg"><img src="{pre}images/hero-tower.jpg" alt="" width="2500" height="1875" style="object-position: 83.5638% 35.5%" fetchpriority="high"></div>
      <div class="wrap"><div class="content medium align-right">
        <div class="block text-right">
          <h1>Telecommunication Infrastructure &amp; Quality Management Services</h1>
        </div>
      </div></div>
    </section>

    <section class="section small">
      <div class="wrap"><div class="content narrow">
        <div class="block">
          <h2>Contracting Services for Installations, Decommissions and more.</h2>
          <p>ABA Ventures specializes in helping nationwide clients manage large scale projects aimed at maintaining and updating telecommunication equipment. We ensure quality installation, decommission, and maintenance services to meet the demands within this quickly growing and changing industry. By providing trusted in-house crews, we ensure quality control and establish a company culture upholding safety awareness, meticulous attention to work, and comprehensive documentation of results.</p>
        </div>
      </div></div>
    </section>

    <section class="section spacer-section" aria-hidden="true"></section>

    <section class="section medium theme-dark">
      <div class="wrap"><div class="content narrow">
        <div class="block">
          <h2>Let&rsquo;s Work Together</h2>
          <p>We&rsquo;re always looking for new opportunities and are comfortable working nationwide. Please get in touch and one of our project managers will contact you about beginning the proposal process.</p>
        </div>
        <div class="block">
          <a class="button button-light" href="{pre}contact/">Contact Us</a>
        </div>
      </div></div>
    </section>"""

ABOUT_1 = """<p>At the core of our business model is quality management, coordinating wide-scale projects across the nation. Our use of unique database management software allows us to deliver results to our clients in real-time.</p><p>We provide logistics and execute equipment removals for&nbsp;major telecommunications carriers and their partners.&nbsp;This includes, but is not limited to,&nbsp;equipment deinstallation and cable mining, including BTS, switch, RF and power cable, PBU, battery, ancillary materials extraction and removal services from cell and switch sites.</p><p>ABA Ventures&rsquo; expertise in&nbsp;process management, documentation, safety, enforcement, security, and overall systemic coverage amongst its&nbsp;management teams raises the bar in terms of quality control in the industry.</p>"""
ABOUT_2 = ("<p>Our in-house crews have comprehensive training&nbsp;in both the technical aspect of our work as well as in the importance of safety awareness. Certifications obtained by our employees&nbsp;include:</p>"
           f'<ul class="bullets">{bullets(["OSHA 10 Hour Course", "OSHA 30 Hour Course", "RF Safety Awareness course", "CPR/First Aid Training", "Verizon Air 21-32 Swap Course"])}</ul>')
ABOUT_3 = "<p>We hold our employees and crew members to the highest standards and best practices, as established by Federal and State laws, industry certification and oversight groups, and company policies. We reinforce the importance of upholding the highest level of safety awareness and hazard recognition on work sites. We have implemented a system of policy communication, awareness training, continuing education, inspections, audits, and proper documentation to ensure full compliance with our company&rsquo;s high standards.</p>"

ABOUT = f"""    <section class="section medium">
      <div class="wrap"><div class="content">
        <div class="block text-center"><h2>About Us</h2></div>
{SPACER}
{figure("collage", False, "about-1.jpg", "Communication towers on top of a green hillside", 1800, 1144, "", ABOUT_1)}
{SPACER}
{figure("collage", True, "about-personnel.jpg", "Crew members in hard hats and safety vests at a construction site", 1800, 1200, "Highly trained personnel", ABOUT_2)}
      </div></div>
    </section>

    <section class="section medium">
      <div class="wrap"><div class="content">
{figure("collage", False, "about-safety.jpg", "CPR training on a practice mannequin", 1800, 1350, "Safety", ABOUT_3)}
      </div></div>
    </section>"""

DECOM = ["In-Shelter Equipment Removals", "BTS &amp; Power Cabinet", "Deinstallation", "Cable Mining",
         "Battery Management &amp; Recycling", "Tower Decommissioning", "Site Surveys",
         "Hazmat Handling and Management", "Concrete Demolition &amp; Removal",
         "Complex Logistics and Materials", "Transport", "Site Restoral", "Detailed Closeout &amp; Reporting"]
EXP = ["ACO", "Additional Carrier", "Battery Integration/Installation/Replacement/Testing", "Cable Laying",
       "Cable Pulling", "DC Power", "Decomm", "Drive Testing", "E-911",
       "Electric power systems installation or service", "Fiber Testing", "GSM", "LTE", "Maintenance",
       "Microwave", "Power cable installation", "Small Cell", "Split Sector", "Structural Mods", "T-1",
       "UMTS", "Wireless"]

SVC_1 = ("<p>We provide quality management solutions for clients, utilizing technology to seamlessly execute projects and coordinate with team members.</p><p>Services include:</p>"
         f'<ul class="bullets">{bullets(["Project management", "Crew oversight", "Construction management"])}</ul>')
SVC_2 = ("<p>ABA specializes in cell site decommissioning, providing high efficiency site removal execution and project logistics.</p><p>Services include:</p>"
         f'<ul class="bullets">{bullets(DECOM)}</ul>')
SVC_3 = "<p>" + "<br>".join(EXP) + "</p>"

SERVICES = f"""    <section class="section medium">
      <div class="wrap"><div class="content">
        <div class="block text-center"><h2>Our services</h2></div>
{SPACER}
{figure("split", False, "services-management.jpg", "Project planning with laptops and paperwork", 1400, 934, "Management Services", SVC_1)}
{SPACER}
{figure("split", True, "services-decommissioning.jpg", "Excavator beside a lattice tower at a cell site at sunset", 1400, 808, "Decommissioning Services", SVC_2)}
{figure("split", False, "services-experience.jpg", "Base of a tower with cable runs inside a fenced cell site at sunset", 1400, 1869, "Experience with:", SVC_3)}
      </div></div>
    </section>"""


def req():
    return '<span class="req">(required)</span>'


CONTACT = f"""    <section class="section medium">
      <div class="wrap"><div class="content">
        <div class="row">
          <div class="col col-5">
            <div class="block"><h2>Contact Us</h2></div>
            <div class="block"><hr></div>
            <div class="block">
              <p><a href="mailto:Austen@abaventures.net" style="text-decoration:none">Austen@abaventures.net</a><br><a href="tel:+19196335235" style="text-decoration:none">(919)-633-5235</a></p>
              <p><a href="mailto:William@abaventures.net" style="text-decoration:none">William@abaventures.net</a><br><a href="tel:+14042165234" style="text-decoration:none">(404)216-5234</a></p>
              <p><a href="mailto:Ashton@abaventures.net" style="text-decoration:none">Ashton@abaventures.net</a></p>
            </div>
            <div class="block"><hr></div>
            <div class="block"></div>
          </div>
          <div class="col col-1"><div class="block spacer" aria-hidden="true"></div></div>
          <div class="col col-6">
            <div class="block" id="contact-form">
              <form class="form" action="https://formsubmit.co/{FORM_TO}" method="POST">
                <input type="hidden" name="_subject" value="New message from abaventures.net">
                <input type="hidden" name="_template" value="table">
                <input type="hidden" name="_captcha" value="false">
                <input type="hidden" name="_next" value="{SITE}/contact/?sent=1">
                <input class="honey" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">
                <fieldset>
                  <legend>Name</legend>
                  <div class="pair">
                    <label class="field"><span class="caption">First Name{req()}</span><input type="text" name="First Name" autocomplete="given-name" required></label>
                    <label class="field"><span class="caption">Last Name{req()}</span><input type="text" name="Last Name" autocomplete="family-name" required></label>
                  </div>
                </fieldset>
                <label class="field"><span class="title">Email{req()}</span><input type="email" name="email" autocomplete="email" required></label>
                <label class="field"><span class="title">Subject{req()}</span><input type="text" name="Subject" required></label>
                <label class="field"><span class="title">Message{req()}</span><textarea name="Message" required></textarea></label>
                <fieldset>
                  <legend>Phone</legend>
                  <label class="field"><input type="tel" name="Phone" autocomplete="tel" aria-label="Phone"></label>
                </fieldset>
                <button class="button button-dark" type="submit">Submit</button>
              </form>
              <p class="form-sent">Thank you!</p>
            </div>
          </div>
        </div>
      </div></div>
    </section>
    <script>
      (function () {{
        var form = document.querySelector(".form");
        form.querySelector('[name="_next"]').value = location.origin + location.pathname + "?sent=1";
        if (/[?&]sent=1/.test(location.search)) document.getElementById("contact-form").classList.add("sent");
      }})();
    </script>"""

page("", "Home", "ABA Ventures provides telecommunication infrastructure contracting and quality management services nationwide: installations, cell site decommissioning, and project management.", HOME)
page("about/", "About", "About ABA Ventures: quality-managed telecom equipment removal, logistics, and in-house crews trained in OSHA, RF safety, and carrier-specific procedures.", ABOUT)
page("services/", "Services", "ABA Ventures services: project and construction management, cell site decommissioning, cable mining, battery recycling, site restoral, and closeout reporting.", SERVICES)
page("contact/", "Contact", "Contact ABA Ventures to start the proposal process for telecommunication infrastructure and decommissioning projects nationwide.", CONTACT)

NOT_FOUND = """    <section class="section medium">
      <div class="wrap"><div class="content narrow">
        <div class="block">
          <h2>Page not found</h2>
          <p>That page doesn&rsquo;t exist. Head back to the <a href="/">home page</a> or <a href="/contact/">contact us</a>.</p>
        </div>
      </div></div>
    </section>"""
page("404/", "Page not found", "Page not found.", NOT_FOUND, pre="/", path="404.html", extra_head='\n  <meta name="robots" content="noindex">')
