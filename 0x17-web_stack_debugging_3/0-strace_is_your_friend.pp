# This Puppet manifest fixes the file permissions for the Apache web root directory
# to resolve a 500 Internal Server Error caused by permission issues.

# Ensure that the directory /var/www/html exists and has the correct permissions.
file { '/var/www/html':
  ensure  => directory,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0755',
  recurse => true,
}

# Restart the Apache service to apply changes
service { 'apache2':
  ensure     => running,
  enable     => true,
  subscribe  => File['/var/www/html'],
}
