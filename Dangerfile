warn "#{gitlab.html_link("requirements.txt")} was edited." if git.modified_files.include? "requirements.txt"
warn "#{gitlab.html_link("requirements-dev.txt")} was edited." if git.modified_files.include? "requirements-dev.txt"
warn "#{gitlab.html_link("requirements-doc.txt")} was edited." if git.modified_files.include? "requirements-doc.txt"


if git.modified_files.include? "config/*.js"
  config_files = git.modified_files.select { |path| path.include? "config/" }
  message "This merge-request changes #{ gitlab.html_link(config_files) }"
end

message "Welcome, #{ gitlab.mr_author }." if gitlab.mr_author == "lordoftheflies"

can_merge = gitlab.mr_json["mergeable"]
warn("This merge-request cannot be merged yet.") unless can_merge

has_milestone = gitlab.mr_json["milestone"] != nil
warn("This merge-request does not refer to an existing milestone", sticky: true) unless has_milestone

failure "Please re-submit this merge-request to develop, we may have already fixed your issue." if gitlab.branch_for_merge != "develop"

failure "Please provide a summary in the Merge Request description" if gitlab.mr_body.length < 5

warn "This merge-request does not have any assignees yet." unless gitlab.mr_json["assignee"]

failure "Please add labels to this merge-request" if gitlab.mr_labels.empty?

declared_trivial = (gitlab.mr_title + gitlab.mr_body).include?("#trivial")

warn "Merge-request is classed as Work in Progress" if gitlab.mr_title.include? "[WIP]"
