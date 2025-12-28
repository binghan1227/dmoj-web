from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import User
from django.contrib.flatpages.models import FlatPage
from judge.admin.comments import CommentAdmin
from judge.admin.contest import ContestAdmin
from judge.admin.contest import ContestParticipationAdmin
from judge.admin.contest import ContestTagAdmin
from judge.admin.interface import BlogPostAdmin
from judge.admin.interface import FlatPageAdmin
from judge.admin.interface import LicenseAdmin
from judge.admin.interface import LogEntryAdmin
from judge.admin.interface import NavigationBarAdmin
from judge.admin.organization import ClassAdmin
from judge.admin.organization import OrganizationAdmin
from judge.admin.organization import OrganizationRequestAdmin
from judge.admin.problem import ProblemAdmin
from judge.admin.problem import ProblemPointsVoteAdmin
from judge.admin.profile import ProfileAdmin
from judge.admin.profile import UserAdmin
from judge.admin.runtime import JudgeAdmin
from judge.admin.runtime import LanguageAdmin
from judge.admin.submission import SubmissionAdmin
from judge.admin.taxon import ProblemGroupAdmin
from judge.admin.taxon import ProblemTypeAdmin
from judge.admin.ticket import TicketAdmin
from judge.models import BlogPost
from judge.models import Class
from judge.models import Comment
from judge.models import CommentLock
from judge.models import Contest
from judge.models import ContestParticipation
from judge.models import ContestTag
from judge.models import Judge
from judge.models import Language
from judge.models import License
from judge.models import MiscConfig
from judge.models import NavigationBar
from judge.models import Organization
from judge.models import OrganizationRequest
from judge.models import Problem
from judge.models import ProblemGroup
from judge.models import ProblemPointsVote
from judge.models import ProblemType
from judge.models import Profile
from judge.models import Submission
from judge.models import Ticket

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(CommentLock)
admin.site.register(Contest, ContestAdmin)
admin.site.register(ContestParticipation, ContestParticipationAdmin)
admin.site.register(ContestTag, ContestTagAdmin)
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
admin.site.register(Judge, JudgeAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(License, LicenseAdmin)
admin.site.register(LogEntry, LogEntryAdmin)
admin.site.register(MiscConfig)
admin.site.register(NavigationBar, NavigationBarAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(OrganizationRequest, OrganizationRequestAdmin)
admin.site.register(Problem, ProblemAdmin)
admin.site.register(ProblemGroup, ProblemGroupAdmin)
admin.site.register(ProblemPointsVote, ProblemPointsVoteAdmin)
admin.site.register(ProblemType, ProblemTypeAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Submission, SubmissionAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
