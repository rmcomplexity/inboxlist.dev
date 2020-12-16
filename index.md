---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
---
<div class="landing-page-wrapper">
  <div class="landing-page-box">
    <h1 class="logo"><i class="fas fa-inbox">&nbsp;</i> Inbox List Dev</h1>
    <div class="logo-font">
      <span>
        By <a href="https://twitter.com/rmcomplexity" target="_blank">
            rmcomplexity
        </a>
      </span>
    </div>
    <div class="pitch-and-form">
       <div class="pitch"> 
        <div class="pitch-image">
            <img src="/assets/svgs/mobile_inbox.svg" alt="Your happy inbox." />
        </div>
        <div class="pitch-copy">
          <h2>
            A newsletter directory for everything Dev.
          </h2>
          <p>
            Newsletters deliver great value through content but is difficult to find the best ones out there.
            <i class="fas fa-inbox">&nbsp;</i> <span class="logo-font">Inbox List Dev</span> curates the best newsletters and organizes them by topics. Now you can easily search and subscribe to great newsletters easily and get awesome content in your inbox.
          </p>
        </div>
      </div>
       <div class="form">
        <h2 class="form-title">
          Get notified at launch!
        </h2>
        <div class="form-content">
            {% include signup_form.html %}
        </div>
       </div>
    </div>
  </div>
</div>
