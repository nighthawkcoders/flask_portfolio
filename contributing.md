<h1>Welcome to our Contributing Guide</h1>

<h3>About Pull Request<h3/>

When you're finished with the changes, create a pull request, also known as a PR.

Pull requests let you tell others about changes you've pushed to a branch in a repository on GitHub. Once a pull request is opened, you can discuss and review the potential changes with collaborators and add follow-up commits before your changes are merged into the base branch.

When pushing commits to a pull request, don't force push! If other collaborators branch the project before a force push, the force push may overwrite commits that collaborators based their work on.

<h4>Create a pull request:</h4>
Create a pull request to propose and collaborate on changes to a repository. These changes are proposed in a branch, which ensures that the default branch only contains finished and approved work.

When thinking about branches, remember that the base branch is where changes should be applied, the head branch contains what you would like to be applied.

When you change the base repository, you also change notifications for the pull request. Everyone that can push to the base repository will receive an email notification and see the new pull request in their dashboard the next time they sign in.

<h4>Merging a pull request:</h4>
Merge a pull request into the upstream branch when work is completed. Anyone with push access to the repository can complete the merge.

In a pull request, you propose that changes you've made on a head branch should be merged into a base branch. By default, any pull request can be merged at any time, unless the head branch is in conflict with the base branch. 

Steps to merge a pull request:
<ol type="1">
<li>Under your repository name, click  Pull requests.</li>
<li>In the "Pull Requests" list, click the pull request you'd like to merge.</li>
<li>Depending on the merge options enabled for your repository, you can:</li>
<ul>
<li><a href="https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/about-pull-request-merges">Merge all of the commits into the base branch</a> by clicking Merge pull request. If the Merge pull request option is not shown, then click the merge drop down menu and select Create a merge commit.</li>
<li><a href="https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/about-pull-request-merges">Squash the commits into one commit</a> by clicking the merge drop down menu, selecting Squash and merge and then clicking the Squash and merge button.</li>
<li><a href="https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/about-pull-request-merges">Rebase the commits individually onto the base branch</a> by clicking the merge drop down menu, selecting Rebase and merge and then clicking the Rebase and merge button.</li>
</ul>
<li>If prompted, type a commit message, or accept the default message.</li>
For information about the default commit messages for squash merges, see <a href="https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/about-pull-request-merges">"About pull request merges."</a></li>
<li>Click Confirm merge, Confirm squash and merge, or Confirm rebase and merge.</li>
</li>