<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://codex.wordpress.org/Editing_wp-config.php
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define('DB_NAME', 'wordpress');

/** MySQL database username */
define('DB_USER', 'wordpressuser');

/** MySQL database password */
define('DB_PASSWORD', 'Im!r122213219');

/** MySQL hostname */
define('DB_HOST', 'localhost');

/** Database Charset to use in creating database tables. */
define('DB_CHARSET', 'utf8mb4');

/** The Database Collate type. Don't change this if in doubt. */
define('DB_COLLATE', '');

/**#@+
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define('AUTH_KEY',         'dUKqn}kVx@^?BO[nSTKO@_YWyEzZ3^_0|c<(rq<#g&s$NW}aV23u&vWWu&8<dtE,');
define('SECURE_AUTH_KEY',  'bYWG8R.>~Ho|QTe(_eo}X(NV{[g&qivP#nNzFhht/yuI_n^w8+_7L)4=sb.~s-.q');
define('LOGGED_IN_KEY',    '=Li^Y)V)eE< Uufx3@)&RX*HPf`27hB[(5ur/SU#/:gVv&iTf|Yoj$yDi<]v`~Cf');
define('NONCE_KEY',        '.xr*5A}jt@^G s?}`Mi2UM7RrF:>5x.xc}vw B[_qC]E.{R;>$Ew|pz,6!^cdp|}');
define('AUTH_SALT',        'y>{|E!6%GgynW8T_]Lf.&D@T;-eP]Ioovjuu^{ }yEm#b})eX5tg%-nbBtuL&5Hr');
define('SECURE_AUTH_SALT', 'g|(>lO2N-PBAOQvQO2v%<Aff7K[$_i}>jeS=jwOiY*mR`@5Kc4{.UiBJ8*Na #K ');
define('LOGGED_IN_SALT',   '~H?V:&[HflbQdbllESmu!X`C<Qgp#ejD8Ng<7V)Hu#0RjA+?3eo8lRI4z&(7PD&H');
define('NONCE_SALT',       ';^UAXHPV!$g&+9bJ,+zNRlXP_~W*2h DumyI]3p3&YiN8<MB]*W:B2uupJkLn+uZ');

/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix  = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the Codex.
 *
 * @link https://codex.wordpress.org/Debugging_in_WordPress
 */
define('WP_DEBUG', false);

/* That's all, stop editing! Happy blogging. */

/** Absolute path to the WordPress directory. */
if ( !defined('ABSPATH') )
	define('ABSPATH', dirname(__FILE__) . '/');

/** Sets up WordPress vars and included files. */
require_once(ABSPATH . 'wp-settings.php');
