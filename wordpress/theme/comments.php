<div>
    <?php if(have_comments()): ?>
        <h3>Kommentare</h3>

        <div id="comments">
            <?php foreach ($comments as $comment) : ?>
                <div class="comment" id="comment-<?php comment_ID() ?>">
                    <small class="commentmetadata" style="color:grey;"><?php comment_author_link() ?> <strong>|</strong> am <?php comment_date('j. F Y') ?> um <?php comment_time('H:i') ?> Uhr</small>
                    <div style="margin-bottom: 30px;">
                    <?php comment_text() ?>
                    </div>

                    <?php if ($comment->comment_approved == '0') : ?>
                        <strong>Achtung: Dein Kommentar muss erst noch freigegeben werden.</strong><br />
                    <?php endif; ?>
                </div>
            <?php endforeach; ?>
        </div>
    <?php endif; ?>

    <h3 id="respond" >Eigenen Kommentar schreiben</h3>

    <form class="comment-form" action="<?php echo get_option('siteurl'); ?>/wp-comments-post.php" method="post" role="form">
        <div class="form-group">
            <label for="author">Name</label>
            <input type="text" name="author" id="author" class="form-control input-small" value="<?php echo $comment_author; ?>" size="22" tabindex="1"/>
        </div>
        <div class="form-group">
            <label for="email">Email <small>(wird nicht gezeigt)</small></label>
            <input type="text" name="email" id="email" class="form-control input-small" value="<?php echo $comment_author_email; ?>" size="22" tabindex="2" />
        </div>
        <div class="form-group">
            <label for="url">Webseite</label>
            <input type="text" name="url" id="url" class="form-control input-small" value="<?php echo $comment_author_url; ?>" size="22" tabindex="3" />
        </div>
        <div class="form-group">
            <label for="comment">Kommentar</label>
            <textarea name="comment" id="comment" class="form-control" style="width: 100%;" rows="10" tabindex="4"></textarea>
        </div>
        <div class="form-group">
            <input name="submit" type="submit" id="submit" tabindex="5" value="Kommentar abschicken" class="btn btn-primary"/>
            <input type="hidden" name="comment_post_ID" class="form-control" value="<?php echo $id; ?>" />
        </div>

        <?php do_action('comment_form', $post->ID); ?>
    </form>
</div>
