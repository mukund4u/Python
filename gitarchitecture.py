# Git Architecture
# Component	Description
# Working-Directory(working space)  --->	Where developers make changes
# Staging-Area --->	        Temporary area before committing changes
# Local-Repository --->	    Stores commits and version history locally
# Remote-Repository --->	Hosted repository (e.g., GitHub) for collaboration
# Git-Objects --->	        Blob, Tree, Commit, Tag for tracking changes
# Branching --->	        Supports parallel development


# Git Configuration

# Level	              Scope	                                                Command Example
# System (--system)	  Applies to all users on the machine	                git config --system user.name "John Doe"
# Global (--global)	  Applies to all repositories for the current user	    git config --global user.email "john@example.com"
# Local (--local)	  Applies only to the specific repository	            git config --local core.editor "vim"
# git config --list	View all configurations
# git config --global --unset core.editor --> to reset


# Git Reset & Revert

# Feature	                git reset	                                git revert
# Effect on History	    Rewrites history (dangerous if pushed)	    Preserves history (safer)
                     #  removes all the git commit
# Undo Specific Commit	Moves branch backward	                    Creates a new commit
# Used for	            Removing local changes	                    Undoing changes safely
# Command Example	    git reset --hard HEAD~1	                    git revert HEAD
# Best for	            Local undo before pushing	                Public/shared branches

# Use git reset when:
# ✅ You haven’t pushed changes yet.
# ✅ You want to remove commits permanently.

# ✔ Use git revert when:
# ✅ You have pushed changes to a shared repo.
# ✅ You want to undo a commit safely without losing history.