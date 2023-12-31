#!/usr/bin/env python3
"""Task 3's module"""
from flask import Flask, request
from typing import List, TypeVar
import os


class Auth:
    """ Manage the API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Returns False """
        if path is None:
            return True
        if excluded_paths is None or not excluded_paths:
            return True
        for excluded_path in excluded_paths:
            if excluded_path.endswith('*') and \
                    path.startswith(excluded_path[:-1]):
                return False
            elif excluded_path == path:
                return False
            elif excluded_path.endswith('/') and \
                    path.startswith(excluded_path[:-1]):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Returns None """
        if request is None:
            return None
        if "Authorization" not in request.headers:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns None """
        return None

    def session_cookie(self, request=None):
        """Returns a cookie value from a request:"""
        if request and os.getenv('SESSION_NAME'):
            cookie = os.getenv('SESSION_NAME')
            return request.cookies.get(cookie)
        return None
