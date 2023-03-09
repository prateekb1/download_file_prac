```git
git rebase -i HEAD~n
// Where n is the number of commits you want to squash
// This will open a edit mode where you will change 'pick' with 'squash' in the commits you want to squash.
// Exit and save the file
git rebase --continue
// If error
git rebase --edit-todo
```