<?php
/**
 * The template for displaying posts in the Aside post format
 *
 * @since 1.0.0
 */
?>
	<article id="post-<?php the_ID(); ?>" <?php post_class(); ?>>
	    <?php get_template_part( 'content', 'header-pf' ); ?>

	    <div class="entry-content description clearfix">
		    <?php the_content( __( 'ادامه مطلب <span class="meta-nav">&rarr;</span>', 'destin-basic') ); ?>
	    </div><!-- .entry-content -->

	    <?php get_template_part( 'content', 'footer' ); ?>
	</article>