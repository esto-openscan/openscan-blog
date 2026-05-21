#!/usr/bin/env ruby
#
# Optionally derive post update dates from Git history.
#
# Keep this disabled by default during/after migrations: bulk migration commits
# would otherwise make every imported post look newly updated.

Jekyll::Hooks.register :posts, :post_init do |post|
  next unless post.site.config['posts_lastmod_from_git']
  next if post.data.key?('last_modified_at')

  commit_num = `git rev-list --count HEAD "#{ post.path }"`

  if commit_num.to_i > 1
    lastmod_date = `git log -1 --pretty="%ad" --date=iso "#{ post.path }"`
    post.data['last_modified_at'] = lastmod_date
  end

end
