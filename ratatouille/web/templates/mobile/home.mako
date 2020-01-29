## -*- coding: utf-8; mode: html; -*-
<%inherit file="tailbone:templates/mobile/home.mako" />

<div style="text-align: center;">
  ## ${h.image(request.static_url('ratatouille.web:static/img/ratatouille.jpg'), "Ratatouille Logo", width='300')}
  ${h.image(request.static_url('tailbone:static/img/home_logo.png'), "Rattail Logo", width='400')}
  <h3>Welcome to ${self.app_title()}</h3>
</div>
