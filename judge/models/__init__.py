from judge.models.comment import Comment
from judge.models.contest import Contest
from judge.models.contest import ContestProblem
from judge.models.interface import BlogPost
from judge.models.problem import LanguageLimit
from judge.models.problem import Problem
from judge.models.problem import Solution
from judge.models.profile import Organization
from judge.models.profile import Profile
from judge.models.runtime import Judge
from judge.models.runtime import Language
from reversion import revisions

revisions.register(Profile, exclude=['points', 'last_access', 'ip', 'rating'])
revisions.register(Problem, follow=['language_limits'])
revisions.register(LanguageLimit)
revisions.register(Contest, follow=['contest_problems'])
revisions.register(ContestProblem)
revisions.register(Organization)
revisions.register(BlogPost)
revisions.register(Solution)
revisions.register(Judge, fields=['name', 'created', 'auth_key', 'description'])
revisions.register(Language)
revisions.register(Comment, fields=['author', 'time', 'page', 'score', 'body', 'hidden', 'parent'])
del revisions
