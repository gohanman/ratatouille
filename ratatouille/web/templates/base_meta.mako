## -*- coding: utf-8; mode: html; -*-
<%inherit file="tailbone:templates/base_meta.mako" />

## default behavior is to read app_title from settings
## <%def name="app_title()">Ratatouille</%def>

<%def name="favicon()">
  ## <link rel="icon" type="image/x-icon" href="${request.static_url('ratatouille.web:static/favicon.ico')}" />
  <link rel="icon" type="image/x-icon" href="${request.static_url('tailbone:static/img/rattail.ico')}" />
</%def>

<%def name="header_logo()">
  ${h.image(request.static_url('tailbone:static/img/rattail.ico'), "Header Logo", style="height: 49px;")}
</%def>

<%def name="footer()">
  <p class="has-text-centered">
    ${h.link_to("Ratatouille {}{}".format(ratatouille.__version__, '' if request.rattail_config.production() else '+dev'), url('about'))}
  </p>
</%def>
