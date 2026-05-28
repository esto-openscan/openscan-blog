#!/usr/bin/env ruby
#
# Optionally derive post update dates from Git history.
#
# Migrated Shopify posts keep redirect_from entries. Skip them by default so
# migration cleanup commits do not make the whole archive look newly updated.
# Set `track_lastmod: true` in a migrated post to opt it back in.

Jekyll::Hooks.register :site, :post_read do |site|
  next unless site.config['posts_lastmod_from_git']

  site.posts.docs.each do |post|
    next if post.data.key?('last_modified_at')
    next if post.data.key?('redirect_from') && !post.data['track_lastmod']

    commit_num = `git rev-list --count HEAD "#{ post.path }"`

    if commit_num.to_i > 1
      lastmod_date = `git log -1 --pretty="%ad" --date=iso "#{ post.path }"`
      post.data['last_modified_at'] = lastmod_date
    end
  end
end
