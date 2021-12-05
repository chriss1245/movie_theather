# A cinema web page


<img width="800" src="https://github-readme-stats.vercel.app/api/pin/?username=chriss1245&repo=movie_theather&theme=vue-dark" align="center"/>
A full web server running in python.

## Backend technologies
 - flask framework
 - sql-alchemy
 - mariadb.

## Frontend technologies
 - html
 - css
 - javascript
 
### Folder structure

movie_theather

    - __init__.py
    - main.py: general controller
    - data.py: our rest api for asking data 
    - model.py: will contain the database structure we have
    - analytics.py: methods for NLP sentiment analysis of site reviews and average movie ratings, generation of encoded pie chart and bar plot
    to be shown in administrator view
    - utils.py: contain some functions needed but not quite realted
    - flask_init.sh & flask_init.ps1: exports the needed environment variables for running flask, we still     need to execute flask run
    - .gitignore: list with files we do not want to be at the repository
    - requirements.txt: list of all the dependencies (python -m pip install -r requirements.txt: automates the install of these dependencies)
    documentation
        - all the manuals and stuff to take into account
    static
        - css files
        img
            - all the images we will need
        js
            - js files
    templates
        main
            - all the views we are going to show
        src
            - html files that can be included or inherited for our main views


### Additional functionalities implemented
From the main page:
 - Search bar
 - Button to sort movies based on an specific criteria
 - Navigation Bar

From customer view:
 - Display of profile picture and user information
 - Button to cancel reservations 
 - Ability for users to write site reviews

From Administrator view:
 - Pie chart in which the amount of neutral, positive and negative reviews is shown, using NLP, passed as a base64 encoded version of the graph generated in matplotlib

From a security stand point:
 - Added Jinja directive to prevent cross-site scripting
 - Included flask_talisman to ensure security that fits the needs of the webpage, control security protocols only allows uploads of images with unknown origin, headers kept with default options: 
    force_https, default True, forces all non-debug connects to https (about HTTPS).
   force_https_permanent, default False, uses 301 instead of 302 for https redirects.
   frame_options, default SAMEORIGIN, can be SAMEORIGIN, DENY, or ALLOWFROM (about Frame Options).
   frame_options_allow_from, default None, a string indicating the domains that are allowed to embed the site via iframe.
   strict_transport_security, default True, whether to send HSTS headers (about HSTS).
   strict_transport_security_preload, default False, enables HSTS preloading. If you register your application with Google's HSTS preload list, Firefox and Chrome will never load your site over a non-secure connection.
   strict_transport_security_max_age, default ONE_YEAR_IN_SECS, length of time the browser will respect the HSTS header.
   strict_transport_security_include_subdomains, default True, whether subdomains should also use HSTS.
   content_security_policy, default default-src: 'self'`, 'object-src': 'none', see the Content Security Policy section (about Content Security Policy).
   content_security_policy_nonce_in, default []. Adds a per-request nonce value to the flask request object and also to the specified CSP header section. I.e. ['script-src', 'style-src']
   content_security_policy_report_only, default False, whether to set the CSP header as "report-only" (as Content-Security-Policy-Report-Only) to ease deployment by disabling the policy enforcement by the browser, requires passing a value with the content_security_policy_report_uri parameter
   content_security_policy_report_uri, default None, a string indicating the report URI used for CSP violation reports
   referrer_policy, default strict-origin-when-cross-origin, a string that sets the Referrer Policy header to send a full URL when performing a same-origin request, only send the origin of the document to an equally secure destination (HTTPS->HTTPS), and send no header to a less secure destination (HTTPS->HTTP) (about Referrer Policy).
   feature_policy, default {}, see the Feature Policy section (about Feature Policy).
   permissions_policy, default {'interest-cohort': '()'}, see the Permissions Policy section (about Permissions Policy).
   document_policy, default {}, see the Document Policy section (about Document Policy).
   session_cookie_secure, default True, set the session cookie to secure, preventing it from being sent over plain http (about cookies (https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie)_).
   session_cookie_http_only, default True, set the session cookie to httponly, preventing it from being read by JavaScript.
   session_cookie_samesite, default Lax, set this to Strict to prevent the cookie from being sent by the browser to the target site in all cross-site browsing context, even when following a regular link.
   force_file_save, default False, whether to set the X-Download-Options header to noopen to prevent IE >= 8 to from opening file downloads directly and only save them instead.
   x_content_type_options, default True, Protects against MIME sniffing vulnerabilities (about Content Type Options).
   x_xss_protection, default True, Protects against cross-site scripting (XSS) attacks (about XSS Protection).


