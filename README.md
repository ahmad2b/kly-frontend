This is a [Next.js](https://nextjs.org/) project bootstrapped with [`create-next-app`](https://github.com/vercel/next.js/tree/canary/packages/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/basic-features/font-optimization) to automatically optimize and load Inter, a custom Google Font.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js/) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/deployment) for more details.

---

JSON Web Key Set (JWKS) is a set of keys that contains the cryptographic keys used to verify any JSON Web Token (JWT) issued by the authorization server. These keys are used to sign and validate JWTs.

JWTs are a compact, URL-safe means of representing claims to be transferred between two parties. They are often used for authentication and information exchange. The claims in a JWT are encoded as a JSON object that is digitally signed using JSON Web Signature (JWS).

JWKS is not an alternative to JWT, but rather a companion to it. When a JWT is issued, it is signed using a key. The recipient of the JWT can then use the JWKS to get the public key and verify the JWT's signature, ensuring it was indeed issued by the expected party and has not been tampered with.

Here's a simplified flow:

A client sends a request to an authorization server to authenticate.
The server authenticates the client, creates a JWT with the necessary claims, and signs it using a private key.
The server sends the JWT back to the client.
The client sends the JWT in the Authorization header when making requests to a resource server.
The resource server fetches the JWKS from the authorization server.
The resource server uses the public key in the JWKS to verify the signature of the JWT.
If the signature is valid, the server processes the request. If not, the server rejects the request.
In the code you provided, the get_jwks() function is used to fetch the JWKS, either from a cache or from a remote server. This JWKS can then be used to verify the signatures of incoming JWTs.

---

To update the tables in the database after adding a new field to the User SQLModel, you would typically use a migration tool. However, SQLModel doesn't have built-in support for migrations yet.

You can manually update the tables by dropping the existing table and recreating it with the new schema. This can be done by modifying the create_db_and_tables function in the \_database.py file.

Here's how you can do it:

Please note that this will delete all existing data in the User table. If you want to preserve the data, you'll need to write a script to backup the data before dropping the table and then restore it after the table is recreated.

For more complex migrations, you might want to consider using Alembic, a database migration tool for SQLAlchemy (which SQLModel is built on). However, using Alembic with SQLModel might require some additional configuration and isn't as straightforward as using it with SQLAlchemy directly.
