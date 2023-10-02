module.exports = ({ env }) => ({
  auth: {
    secret: env('v1.0-ef78cc1e2373106e4db2a85a-ff61d18d601e6660163d573fd4bd36d9ca6def6be4c4333f040ee7085de7b998a01c5232a32bdb959c44ddfc3bec4f93967d5568ec448fe1e4291081268499dbd58c4c5e43f6528647'),
  },
  apiToken: {
    salt: env('6a58a402f5ceb674c9ca870a7b7c9a6d1ce61'),
  },
  transfer: {
    token: {
      salt: env('f6cb7c65-5ab3-4e09-99df-813974f416af-0.1.1-integration-token'),
    },
  },
});
