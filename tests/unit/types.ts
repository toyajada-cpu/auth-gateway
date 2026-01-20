export enum OAuthFlow {
  ClientCredentials,
  AuthorizationCode,
  Implicit,
  RefreshToken,
}

export enum TokenType {
  Bearer,
  Refresh,
}

export enum AuthError {
  Unauthorized,
  InvalidCredentials,
  InvalidGrant,
  InternalServerError,
}

export enum AuthEvent {
  TokenIssued,
  ErrorOccurred,
}

export interface OAuthConfig {
  publicClientId: string;
  privateClientId: string;
  privateClientSecret: string;
}

export interface RefreshToken {
  token: string;
  refreshToken: string;
  expiresAt: Date;
}

export interface AccessToken {
  token: string;
  type: TokenType;
  expiresAt: Date;
}

export interface User {
  sub: string;
  name: string;
  email: string;
  emailVerified: boolean;
  picture: string;
}