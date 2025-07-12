# Vercel Deployment Guide 🚀

This guide will help you deploy your AI Career Recommendation System to Vercel.

## Prerequisites

1. **GitHub Repository**: Your project is already on GitHub at https://github.com/belloibrahv/rml
2. **Vercel Account**: Sign up at [vercel.com](https://vercel.com)

## Step 1: Connect to Vercel

1. Go to [vercel.com](https://vercel.com) and sign in
2. Click "New Project"
3. Import your GitHub repository: `belloibrahv/rml`
4. Vercel will automatically detect it's a Python project

## Step 2: Configure Deployment Settings

### Build Settings
- **Framework Preset**: Other
- **Build Command**: Leave empty (Vercel will auto-detect)
- **Output Directory**: Leave empty
- **Install Command**: `pip install -r requirements.txt`

### Environment Variables
Add these environment variables in the Vercel dashboard:
```
FLASK_ENV=production
FLASK_DEBUG=0
```

## Step 3: Deploy

1. Click "Deploy"
2. Vercel will build and deploy your application
3. You'll get a URL like: `https://your-project-name.vercel.app`

## Step 4: Custom Domain (Optional)

1. In your Vercel dashboard, go to "Settings" → "Domains"
2. Add your custom domain
3. Follow the DNS configuration instructions

## Project Structure for Vercel

The project has been configured with these files:

- `vercel.json`: Vercel configuration
- `api/index.py`: API handler for Vercel
- `requirements.txt`: Python dependencies
- `runtime.txt`: Python version specification

## Troubleshooting

### Common Issues

1. **Build Failures**
   - Check that all dependencies are in `requirements.txt`
   - Ensure Python version is compatible (3.9+)

2. **Import Errors**
   - Make sure all imports use relative paths
   - Check that `api/index.py` can import from `backend/app/app.py`

3. **Static Files Not Loading**
   - Verify static files are in `backend/app/static/`
   - Check the routes in `vercel.json`

### Debugging

1. **Check Build Logs**
   - Go to your Vercel dashboard
   - Click on the latest deployment
   - Check the build logs for errors

2. **Local Testing**
   ```bash
   # Install Vercel CLI
   npm i -g vercel
   
   # Test locally
   vercel dev
   ```

## Environment Variables

For production, consider setting these in Vercel:

```
FLASK_ENV=production
FLASK_DEBUG=0
DATABASE_URL=your_database_url
```

## Database Considerations

⚠️ **Important**: SQLite databases don't work well with Vercel's serverless functions because:
- They're read-only in production
- Data doesn't persist between function calls
- File system access is limited

### Solutions:

1. **Use External Database** (Recommended)
   - PostgreSQL (Supabase, Railway, etc.)
   - MongoDB Atlas
   - Firebase Firestore

2. **Disable Database Features** (Temporary)
   - Comment out database operations
   - Use in-memory storage for testing

## Performance Optimization

1. **Cold Start Optimization**
   - Keep dependencies minimal
   - Use lightweight libraries

2. **Caching**
   - Implement response caching
   - Use CDN for static files

3. **Monitoring**
   - Set up Vercel Analytics
   - Monitor function execution times

## Security

1. **Environment Variables**
   - Never commit sensitive data
   - Use Vercel's environment variable system

2. **Input Validation**
   - Validate all user inputs
   - Implement rate limiting

3. **HTTPS**
   - Vercel provides HTTPS by default
   - No additional configuration needed

## Post-Deployment

1. **Test All Features**
   - Career recommendation API
   - Static file serving
   - Form submissions

2. **Monitor Performance**
   - Check Vercel Analytics
   - Monitor error rates

3. **Update Documentation**
   - Update README with live URL
   - Document any deployment-specific notes

## Support

If you encounter issues:

1. Check Vercel's documentation: https://vercel.com/docs
2. Review build logs in Vercel dashboard
3. Test locally with `vercel dev`
4. Check GitHub issues for similar problems

## Success Checklist

- [ ] Repository connected to Vercel
- [ ] Build successful
- [ ] Application accessible via URL
- [ ] All features working
- [ ] Custom domain configured (optional)
- [ ] Environment variables set
- [ ] Performance optimized
- [ ] Documentation updated

Your application should now be live and accessible worldwide! 🌍 