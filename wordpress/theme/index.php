<?php get_header(); ?>

<div class="container blog">
    <?php if (have_posts()) : while (have_posts()) : the_post(); ?>
        <div class="post row">
            <div class="col-md-9">
                <h2>
                    <a href="<?php the_permalink(); ?>">
                        <?php the_title(); ?>
                    </a>
                </h2>
                <div class="post-content">
                    <?php the_content(); ?>

                    <div class="date post-footer">
                        <?php the_author(); ?> | <?php the_date(); ?>
                    </div>
                </div>
            </div>
        </div>
    <?php endwhile; else: ?>
        <p>Es ist kein Eintrag vorhanden.</p>
    <?php endif; ?>

    <p align="center"><?php posts_nav_link(); ?></p>   
</div>

<?php get_footer(); ?> 