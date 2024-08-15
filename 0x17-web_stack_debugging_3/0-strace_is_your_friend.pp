# This Puppet manifest fixes the file permissions for the Apache web root directory
# to resolve a 500 Internal Server Error caused by permission issues.

exec { 'fix config typo':
  command => "sed -i 's/.phpp/.php/' /var/www/html/wp-settings.php",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
