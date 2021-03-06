## -*- coding: utf-8; mode: html; -*-
<%inherit file="tailbone:templates/mobile/base.mako" />

<%def name="app_title()">Ratatouille</%def>

<%def name="mobile_usermenu()">
  <div id="usermenu" data-role="panel" data-display="overlay">
    <ul data-role="listview">
      <li data-icon="home">${h.link_to("Home", url('mobile.home'))}</li>
      % if request.is_root:
          <li class="root-user" data-icon="forbidden">${h.link_to("Stop being root", url('stop_root'), **{'data-ajax': 'false'})}</li>
      % elif request.is_admin:
          <li class="root-user" data-icon="forbidden">${h.link_to("Become root", url('become_root'), **{'data-ajax': 'false'})}</li>
      % endif
      <li data-icon="lock">${h.link_to("Logout", url('logout'), **{'data-ajax': 'false'})}</li>
      <li data-icon="info">${h.link_to("About {}".format(capture(self.app_title)), url('mobile.about'))}</li>
    </ul>
  </div>
</%def>

<%def name="mobile_footer()">
  <div data-role="footer">
    <h4>${h.link_to("Ratatouille {}{}".format(ratatouille.__version__, '' if request.rattail_config.production() else '+dev'), url('mobile.about'))}</h4>
  </div>
</%def>

${parent.body()}
