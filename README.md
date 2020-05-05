# DRF

## Profiles API

### Basic Requirements:

- Create a new profile
  - Validate profile data
- Listing existing profiles
  - Search for profiles
- Viewing a specific profile given the profile ID
- Update my profile, for logged in user
  - Update name, email address and password.
- Delete Profile -> Archive the record,
  - set the `is_deleted` field to `True` but keep the record

### API URLs

#### URLs for our API

- `/api/v1/profile` - list all profiles
  - GET (list profiles)
  - POST (create profile)
- `/api/v1/profile/<int:profile_id>` - manage specific profile
  - GET (view specific profile)
  - PUT/PATCH (update profile)
  - DELETE (remove profile)

## Feed API
### Basic Requirements
- Creating  new feed items
  - For logged in users only
- Updating feed items
  - For logged in users only
- Delete profile feed items
  - For logged in users only
- Viewing other profile status updates

### API URLs
